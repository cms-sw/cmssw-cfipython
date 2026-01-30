import FWCore.ParameterSet.Config as cms

def sistrip_SiStripClustersToLegacy(*args, **kwargs):
  mod = cms.EDProducer('sistrip::SiStripClustersToLegacy',
    source = cms.InputTag('hltSiStripRawToClustersFacilityAlpaka'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
