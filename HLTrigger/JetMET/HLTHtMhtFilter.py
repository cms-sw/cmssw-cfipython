import FWCore.ParameterSet.Config as cms

def HLTHtMhtFilter(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
