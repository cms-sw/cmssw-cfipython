import FWCore.ParameterSet.Config as cms

def TotemRPClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('TotemRPClusterProducer',
    tagDigi = cms.InputTag('totemRPRawToDigi', 'TrackingStrip'),
    verbosity = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
