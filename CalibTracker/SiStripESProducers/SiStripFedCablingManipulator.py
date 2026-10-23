import FWCore.ParameterSet.Config as cms

def SiStripFedCablingManipulator(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripFedCablingManipulator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
