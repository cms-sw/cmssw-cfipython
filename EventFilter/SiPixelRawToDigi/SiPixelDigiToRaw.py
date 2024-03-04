import FWCore.ParameterSet.Config as cms

def SiPixelDigiToRaw(**kwargs):
  mod = cms.EDProducer('SiPixelDigiToRaw',
    InputLabel = cms.required.InputTag,
    UsePhase1 = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
