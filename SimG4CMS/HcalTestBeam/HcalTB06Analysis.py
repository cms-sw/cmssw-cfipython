import FWCore.ParameterSet.Config as cms

def HcalTB06Analysis(**kwargs):
  mod = cms.EDAnalyzer('HcalTB06Analysis',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
