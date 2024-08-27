import FWCore.ParameterSet.Config as cms

def L1TCaloLayer1(**kwargs):
  mod = cms.EDProducer('L1TCaloLayer1',
    ecalToken = cms.InputTag('simEcalTriggerPrimitiveDigis'),
    hcalToken = cms.InputTag('simHcalTriggerPrimitiveDigis'),
    useLSB = cms.bool(True),
    useCalib = cms.bool(True),
    useECALLUT = cms.bool(True),
    useHCALLUT = cms.bool(True),
    useHFLUT = cms.bool(True),
    useHCALFBLUT = cms.bool(False),
    verbose = cms.untracked.bool(False),
    unpackEcalMask = cms.bool(False),
    unpackHcalMask = cms.bool(False),
    firmwareVersion = cms.int32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
