import FWCore.ParameterSet.Config as cms

def SiStripLorentzAngleReader(**kwargs):
  mod = cms.EDAnalyzer('SiStripLorentzAngleReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
