import FWCore.ParameterSet.Config as cms

def MCTruthCompositeMatcherNew(*args, **kwargs):
  mod = cms.EDProducer('MCTruthCompositeMatcherNew',
    src = cms.required.InputTag,
    matchMaps = cms.required.VInputTag,
    matchPDGId = cms.required.vint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
