import FWCore.ParameterSet.Config as cms

def EtaPtMinPixelMatchGsfElectronFullCloneSelector(**kwargs):
  mod = cms.EDFilter('EtaPtMinPixelMatchGsfElectronFullCloneSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
