import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationByIsolationMVA2 = cms.EDProducer('PFRecoTauDiscriminationByIsolationMVA2',
  verbosity = cms.int32(0),
  Prediscriminants = cms.PSet(
    leadTrack = cms.PSet(),
    decayMode = cms.PSet()
  )
)
