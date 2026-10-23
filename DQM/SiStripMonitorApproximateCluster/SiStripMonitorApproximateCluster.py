import FWCore.ParameterSet.Config as cms

def SiStripMonitorApproximateCluster(*args, **kwargs):
  mod = cms.EDProducer('SiStripMonitorApproximateCluster',
    compareClusters = cms.bool(False),
    ApproxClustersProducer = cms.InputTag('hltSiStripClusters2ApproxClusters'),
    SiStripFEDErrorVector = cms.InputTag('hltSiStripRawToDigi'),
    ClustersProducer = cms.InputTag('hltSiStripClusterizerForRawPrime'),
    folder = cms.string('SiStripApproximateClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
