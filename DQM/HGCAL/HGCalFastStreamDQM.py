import FWCore.ParameterSet.Config as cms

def HGCalFastStreamDQM(*args, **kwargs):
  mod = cms.EDProducer('HGCalFastStreamDQM',
    Raw = cms.InputTag('rawDataCollector'),
    ECONDPacketInfo = cms.InputTag('hgcalDigis'),
    FEDPacketInfo = cms.InputTag('hgcalDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
