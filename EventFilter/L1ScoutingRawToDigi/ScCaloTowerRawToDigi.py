import FWCore.ParameterSet.Config as cms

def ScCaloTowerRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('ScCaloTowerRawToDigi',
    srcInputTag = cms.InputTag('rawDataCollector'),
    sourceIdList = cms.vint32(
      32,
      33,
      34,
      35,
      36,
      37,
      38,
      39,
      40,
      41,
      42,
      43,
      44,
      45,
      46,
      47,
      48,
      49
    ),
    debug = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
