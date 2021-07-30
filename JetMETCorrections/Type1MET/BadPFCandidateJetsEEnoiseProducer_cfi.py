import FWCore.ParameterSet.Config as cms

BadPFCandidateJetsEEnoiseProducer = cms.EDProducer('BadPFCandidateJetsEEnoiseProducer',
  jetsrc = cms.InputTag('slimmedJets'),
  userawPt = cms.bool(True),
  ptThreshold = cms.double(50),
  minEtaThreshold = cms.double(2.65),
  maxEtaThreshold = cms.double(3.139),
  mightGet = cms.optional.untracked.vstring
)
