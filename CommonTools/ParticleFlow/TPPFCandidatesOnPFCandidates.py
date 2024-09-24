import FWCore.ParameterSet.Config as cms

def TPPFCandidatesOnPFCandidates(**kwargs):
  mod = cms.EDProducer('TPPFCandidatesOnPFCandidates',
    enable = cms.required.bool,
    name = cms.untracked.string('No Name'),
    topCollection = cms.required.InputTag,
    bottomCollection = cms.required.InputTag,
    matchByPtrDirect = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod