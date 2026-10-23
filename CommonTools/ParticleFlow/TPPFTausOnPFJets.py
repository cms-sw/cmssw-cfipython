import FWCore.ParameterSet.Config as cms

def TPPFTausOnPFJets(*args, **kwargs):
  mod = cms.EDProducer('TPPFTausOnPFJets',
    enable = cms.required.bool,
    name = cms.untracked.string('No Name'),
    topCollection = cms.required.InputTag,
    bottomCollection = cms.required.InputTag,
    matchByPtrDirect = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
