import FWCore.ParameterSet.Config as cms

def TestDescriptionComments(**kwargs):
  mod = cms.EDAnalyzer('TestDescriptionComments',
    sswitch = cms.string('b'),
    y1 = cms.required.double,
    y2 = cms.required.double,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
