import FWCore.ParameterSet.Config as cms

recoTauDecayModeCutMultiplexer = cms.EDProducer('RecoTauDecayModeCutMultiplexer',
  Prediscriminants = cms.PSet(
    leadTrack = cms.PSet(),
    decayMode = cms.PSet()
  )
)
