import FWCore.ParameterSet.Config as cms

def BadPFCandidateJetsEEnoiseProducer(**kwargs):
  mod = cms.EDProducer('BadPFCandidateJetsEEnoiseProducer',
    jetsrc = cms.InputTag('slimmedJets'),
    userawPt = cms.bool(True),
    ptThreshold = cms.double(50),
    minEtaThreshold = cms.double(2.65),
    maxEtaThreshold = cms.double(3.139),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
