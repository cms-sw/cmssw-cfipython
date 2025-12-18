import FWCore.ParameterSet.Config as cms

def OrbitNanoAODOutputModule(*args, **kwargs):
  mod = cms.OutputModule('OrbitNanoAODOutputModule',
    fileName = cms.required.untracked.string,
    logicalFileName = cms.untracked.string(''),
    compressionLevel = cms.untracked.int32(9),
    compressionAlgorithm = cms.untracked.string('ZLIB'),
    skipEmptyBXs = cms.bool(False),
    saveProvenance = cms.untracked.bool(True),
    fakeNameForCrab = cms.untracked.bool(False),
    autoFlush = cms.untracked.int32(-10000000),
    outputCommands = cms.untracked.vstring(
      'drop *',
      'keep l1ScoutingRun3OrbitFlatTable_*Table_*_*'
    ),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    ),
    dataset = cms.untracked.PSet(),
    branches = cms.PSet(),
    selectedBx = cms.InputTag('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
