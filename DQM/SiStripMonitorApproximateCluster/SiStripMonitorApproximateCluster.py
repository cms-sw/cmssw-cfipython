import FWCore.ParameterSet.Config as cms

def SiStripMonitorApproximateCluster(**kwargs):
  mod = cms.EDProducer('SiStripMonitorApproximateCluster',
    compareClusters = cms.bool(False),
    ApproxClustersProducer = cms.InputTag('hltSiStripClusters2ApproxClusters'),
    SiStripFEDErrorVector = cms.InputTag('hltSiStripRawToDigi'),
    ClustersProducer = cms.InputTag('hltSiStripClusterizerForRawPrime'),
    folder = cms.string('SiStripApproximateClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
