import FWCore.ParameterSet.Config as cms

def ESRawToDigi(**kwargs):
  mod = cms.EDProducer('ESRawToDigi',
    sourceTag = cms.InputTag('rawDataCollector'),
    debugMode = cms.untracked.bool(False),
    InstanceES = cms.string(''),
    LookupTable = cms.FileInPath('EventFilter/ESDigiToRaw/data/ES_lookup_table.dat'),
    ESdigiCollection = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
