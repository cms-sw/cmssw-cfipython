import FWCore.ParameterSet.Config as cms

def HLTHtMhtFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTHtMhtFilter',
    saveTags = cms.bool(True),
    htLabels = cms.VInputTag('hltHtMhtProducer'),
    mhtLabels = cms.VInputTag('hltHtMhtProducer'),
    minHt = cms.vdouble(250),
    minMht = cms.vdouble(70),
    minMeff = cms.vdouble(0),
    meffSlope = cms.vdouble(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
