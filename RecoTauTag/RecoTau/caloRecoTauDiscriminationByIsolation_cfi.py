import FWCore.ParameterSet.Config as cms

caloRecoTauDiscriminationByIsolation = cms.EDProducer('CaloRecoTauDiscriminationByIsolation',
  Prediscriminants = cms.PSet(
    leadTrack = cms.PSet(),
    decayMode = cms.PSet()
  )
)
