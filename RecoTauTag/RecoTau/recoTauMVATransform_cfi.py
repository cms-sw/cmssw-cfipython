import FWCore.ParameterSet.Config as cms

recoTauMVATransform = cms.EDProducer('RecoTauMVATransform',
  Prediscriminants = cms.PSet(
    leadTrack = cms.PSet(),
    decayMode = cms.PSet()
  )
)
