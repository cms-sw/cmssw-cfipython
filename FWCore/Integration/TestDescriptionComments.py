import FWCore.ParameterSet.Config as cms

def TestDescriptionComments(*args, **kwargs):
  mod = cms.EDAnalyzer('TestDescriptionComments',
    sswitch = cms.string('b'),
    y1 = cms.required.double,
    y2 = cms.required.double,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
