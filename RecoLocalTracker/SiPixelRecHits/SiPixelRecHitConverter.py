import FWCore.ParameterSet.Config as cms

def SiPixelRecHitConverter(*args, **kwargs):
  mod = cms.EDProducer('SiPixelRecHitConverter',
    src = cms.InputTag('siPixelClusters'),
    CPE = cms.string('PixelCPEGeneric'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
