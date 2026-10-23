import FWCore.ParameterSet.Config as cms

def LHCInfoProducer(*args, **kwargs):
  mod = cms.EDProducer('LHCInfoProducer',
    lhcInfoLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    useNewLHCInfo = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
