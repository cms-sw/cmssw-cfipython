import FWCore.ParameterSet.Config as cms

esRawToDigi = cms.EDProducer('ESRawToDigi',
  sourceTag = cms.InputTag('rawDataCollector'),
  debugMode = cms.untracked.bool(False),
  InstanceES = cms.string(''),
  LookupTable = cms.FileInPath('EventFilter/ESDigiToRaw/data/ES_lookup_table.dat'),
  ESdigiCollection = cms.string('')
)
