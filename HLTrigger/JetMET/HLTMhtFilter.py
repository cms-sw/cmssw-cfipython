import FWCore.ParameterSet.Config as cms

def HLTMhtFilter(**kwargs):
  mod = cms.EDFilter('HLTMhtFilter',
    saveTags = cms.bool(True),
    mhtLabels = cms.VInputTag('hltMhtProducer'),
    minMht = cms.vdouble(70),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
