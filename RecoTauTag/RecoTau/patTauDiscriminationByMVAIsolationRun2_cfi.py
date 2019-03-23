import FWCore.ParameterSet.Config as cms

patTauDiscriminationByMVAIsolationRun2 = cms.EDProducer('PATTauDiscriminationByMVAIsolationRun2',
  verbosity = cms.int32(0),
  Prediscriminants = cms.PSet(
    leadTrack = cms.PSet(),
    decayMode = cms.PSet()
  )
)
