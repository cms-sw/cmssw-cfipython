import FWCore.ParameterSet.Config as cms

def PtMinGsfElectronCountFilter(**kwargs):
  mod = cms.EDFilter('PtMinGsfElectronCountFilter',
    src = cms.InputTag(''),
    ptMin = cms.double(0),
    minNumber = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
