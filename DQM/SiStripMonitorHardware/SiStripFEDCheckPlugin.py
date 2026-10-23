import FWCore.ParameterSet.Config as cms

def SiStripFEDCheckPlugin(*args, **kwargs):
  mod = cms.EDProducer('SiStripFEDCheckPlugin',
    DirName = cms.untracked.string('SiStrip/FEDIntegrity/'),
    RawDataTag = cms.InputTag('source'),
    HistogramUpdateFrequency = cms.untracked.uint32(1000),
    PrintDebugMessages = cms.untracked.bool(False),
    doPLOTfedsPresent = cms.bool(True),
    doPLOTfedFatalErrors = cms.bool(True),
    doPLOTfedNonFatalErrors = cms.bool(True),
    doPLOTnFEDinVsLS = cms.bool(False),
    doPLOTnFEDinWdataVsLS = cms.bool(False),
    WriteDQMStore = cms.untracked.bool(False),
    DoPayloadChecks = cms.untracked.bool(True),
    CheckChannelLengths = cms.untracked.bool(True),
    CheckChannelPacketCodes = cms.untracked.bool(True),
    CheckFELengths = cms.untracked.bool(True),
    CheckChannelStatus = cms.untracked.bool(True),
    LSBin = cms.int32(5000),
    LSMin = cms.double(0.5),
    LSMax = cms.double(5000.5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
