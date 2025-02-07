import FWCore.ParameterSet.Config as cms

def SiStripRawToDigiModule(*args, **kwargs):
  mod = cms.EDProducer('SiStripRawToDigiModule',
    ProductLabel = cms.InputTag('rawDataCollector'),
    AppendedBytes = cms.int32(0),
    TriggerFedId = cms.int32(0),
    LegacyUnpacker = cms.bool(False),
    UseDaqRegister = cms.bool(False),
    UseFedKey = cms.bool(False),
    UnpackBadChannels = cms.bool(False),
    MarkModulesOnMissingFeds = cms.bool(True),
    FedBufferDumpFreq = cms.untracked.int32(0),
    FedEventDumpFreq = cms.untracked.int32(0),
    Quiet = cms.untracked.bool(True),
    UnpackCommonModeValues = cms.bool(False),
    DoAllCorruptBufferChecks = cms.bool(False),
    DoAPVEmulatorCheck = cms.bool(False),
    ErrorThreshold = cms.uint32(7174),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
