import FWCore.ParameterSet.Config as cms

def MTDDigiGeometryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('MTDDigiGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
