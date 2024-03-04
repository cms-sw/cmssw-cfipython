import FWCore.ParameterSet.Config as cms

def SiStripDigiToRawModule(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
