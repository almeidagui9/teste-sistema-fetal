describe('Fluxo completo do sistema fetal', () => {
  it('Envia dados e exibe resultado da predição', () => {
    cy.visit('http://localhost:3000/')
    cy.get('#cpf').type('12345678900')
    cy.get('#baseline_value').type('120')
    // continue com os demais campos...
    cy.get('#submit').click()
    cy.contains('Situação fetal prevista:').should('be.visible')
  })
})
