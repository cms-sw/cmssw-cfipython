import FWCore.ParameterSet.Config as cms

def SiStripApprox2ApproxClusters(*args, **kwargs):
  mod = cms.EDProducer('SiStripApprox2ApproxClusters',
    inputApproxClusters = cms.InputTag('siStripClusters'),
    approxVersion = cms.string('ORIGINAL'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
