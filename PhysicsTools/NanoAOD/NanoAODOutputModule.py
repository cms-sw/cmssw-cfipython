import FWCore.ParameterSet.Config as cms

def NanoAODOutputModule(**kwargs):
  mod = cms.OutputModule('NanoAODOutputModule',
    fileName = cms.required.untracked.string,
    logicalFileName = cms.untracked.string(''),
    compressionLevel = cms.untracked.int32(9),
    compressionAlgorithm = cms.untracked.string('ZLIB'),
    saveProvenance = cms.untracked.bool(True),
    fakeNameForCrab = cms.untracked.bool(False),
    autoFlush = cms.untracked.int32(-10000000),
    outputCommands = cms.untracked.vstring(
      'drop *',
      'keep nanoaodFlatTable_*Table_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep String_*_genModel_*',
      'keep nanoaodMergeableCounterTable_*Table_*_*',
      'keep nanoaodUniqueString_nanoMetadata_*_*'
    ),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.optional.vstring
    ),
    dataset = cms.untracked.PSet(),
    branches = cms.PSet()
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
