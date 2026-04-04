import FWCore.ParameterSet.Config as cms

def SiStripDigiToRawModule(*args, **kwargs):
  mod = cms.EDProducer('SiStripDigiToRawModule',
    FedReadoutMode = cms.string('ZERO_SUPPRESSED'),
    PacketCode = cms.string('ZERO_SUPPRESSED'),
    UseFedKey = cms.bool(False),
    UseWrongDigiType = cms.bool(False),
    CopyBufferHeader = cms.bool(False),
    InputDigis = cms.InputTag('simSiStripDigis', 'ZeroSuppressed'),
    RawDataTag = cms.InputTag('rawDataCollector'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
