import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationByMVAIsolationRun2 = cms.EDProducer('PFRecoTauDiscriminationByMVAIsolationRun2',
  verbosity = cms.int32(0),
  Prediscriminants = cms.PSet(
    leadTrack = cms.PSet(),
    decayMode = cms.PSet()
  )
)
