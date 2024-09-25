import FWCore.ParameterSet.Config as cms

def CTPPSPixelDigiToRaw(*args, **kwargs):
  mod = cms.EDProducer('CTPPSPixelDigiToRaw',
    isRun3 = cms.bool(True),
    InputLabel = cms.InputTag('RPixDetDigitizer'),
    mappingLabel = cms.string('RPix'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
