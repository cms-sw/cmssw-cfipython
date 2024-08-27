import FWCore.ParameterSet.Config as cms

def SiStripApprox2ApproxClusters(**kwargs):
  mod = cms.EDProducer('SiStripApprox2ApproxClusters',
    inputApproxClusters = cms.InputTag('siStripClusters'),
    approxVersion = cms.string('ORIGINAL'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
