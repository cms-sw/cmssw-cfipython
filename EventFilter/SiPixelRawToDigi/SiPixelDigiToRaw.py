import FWCore.ParameterSet.Config as cms

def SiPixelDigiToRaw(*args, **kwargs):
  mod = cms.EDProducer('SiPixelDigiToRaw',
    InputLabel = cms.required.InputTag,
    UsePhase1 = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
