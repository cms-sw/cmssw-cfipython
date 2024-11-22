import FWCore.ParameterSet.Config as cms

def L1TGlobalSummary(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TGlobalSummary',
    AlgInputTag = cms.InputTag(''),
    ExtInputTag = cms.InputTag(''),
    MinBx = cms.int32(0),
    MaxBx = cms.int32(0),
    DumpTrigResults = cms.bool(False),
    DumpRecord = cms.bool(False),
    DumpTrigSummary = cms.bool(True),
    ReadPrescalesFromFile = cms.bool(False),
    psFileName = cms.string('prescale_L1TGlobal.csv'),
    psColumn = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
