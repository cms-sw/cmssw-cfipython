import FWCore.ParameterSet.Config as cms

def TkInstLumiTableProducer(**kwargs):
  mod = cms.EDProducer('TkInstLumiTableProducer',
    name = cms.string(''),
    doc = cms.string(''),
    extension = cms.bool(False),
    lumiScalers = cms.InputTag('scalersRawToDigi'),
    metadata = cms.InputTag('onlineMetaDataDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
