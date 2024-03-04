import FWCore.ParameterSet.Config as cms

def SiStripFedCablingManipulator(**kwargs):
  mod = cms.EDAnalyzer('SiStripFedCablingManipulator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
