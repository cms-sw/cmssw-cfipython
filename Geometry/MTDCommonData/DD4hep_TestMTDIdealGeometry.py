import FWCore.ParameterSet.Config as cms

def DD4hep_TestMTDIdealGeometry(*args, **kwargs):
  mod = cms.EDAnalyzer('DD4hep_TestMTDIdealGeometry',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
