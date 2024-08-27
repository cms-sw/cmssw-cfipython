import FWCore.ParameterSet.Config as cms

def CSCDCCUnpacker(**kwargs):
  mod = cms.EDProducer('CSCDCCUnpacker',
    InputObjects = cms.InputTag('rawDataCollector'),
    UseExaminer = cms.bool(True),
    ExaminerMask = cms.uint32(535557110),
    UseSelectiveUnpacking = cms.bool(True),
    ErrorMask = cms.uint32(0),
    UnpackStatusDigis = cms.bool(False),
    UseFormatStatus = cms.bool(True),
    useRPCs = cms.bool(False),
    useGEMs = cms.bool(True),
    useCSCShowers = cms.bool(True),
    Debug = cms.untracked.bool(False),
    PrintEventNumber = cms.untracked.bool(False),
    runDQM = cms.untracked.bool(False),
    VisualFEDInspect = cms.untracked.bool(False),
    VisualFEDShort = cms.untracked.bool(False),
    FormatedEventDump = cms.untracked.bool(False),
    SuppressZeroLCT = cms.untracked.bool(True),
    DisableMappingCheck = cms.untracked.bool(False),
    B904Setup = cms.untracked.bool(False),
    B904vmecrate = cms.untracked.int32(1),
    B904dmb = cms.untracked.int32(3),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
