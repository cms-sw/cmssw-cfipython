import FWCore.ParameterSet.Config as cms

def CTPPSPixelDigiToRaw(**kwargs):
  mod = cms.EDProducer('CTPPSPixelDigiToRaw',
    isRun3 = cms.bool(True),
    InputLabel = cms.InputTag('RPixDetDigitizer'),
    mappingLabel = cms.string('RPix'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
