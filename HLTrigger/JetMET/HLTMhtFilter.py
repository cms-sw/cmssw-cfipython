import FWCore.ParameterSet.Config as cms

def HLTMhtFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTMhtFilter',
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag('hltMhtProducer'),
    minMht = cms.vdouble(70),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
