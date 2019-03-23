import FWCore.ParameterSet.Config as cms

pfTauDecayModeCutMultiplexer = cms.EDProducer('PFTauDecayModeCutMultiplexer',
  Prediscriminants = cms.PSet(
    leadTrack = cms.PSet(),
    decayMode = cms.PSet()
  )
)
