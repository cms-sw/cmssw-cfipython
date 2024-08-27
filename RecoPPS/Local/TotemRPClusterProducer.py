import FWCore.ParameterSet.Config as cms

def TotemRPClusterProducer(**kwargs):
  mod = cms.EDProducer('TotemRPClusterProducer',
    tagDigi = cms.InputTag('totemRPRawToDigi', 'TrackingStrip'),
    verbosity = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
